# An trivial application that does nothing
from petr4 import App
from topo import *
from petr4.runtime import *
from tornado.ioloop import *

class MyApp(App):
  def init_topo(self):
    topo = Topology()
    
    topo.add_switch("s1")

    for i in [1,2,3,4]:
      hi = "h" + str(i)
      topo.add_host(hi)
      topo.add_link(hi, "s1", 0, i, 1)

    # compute shortest paths
    paths = topo.e2e_shortest_paths()

    self.topo = topo
    self.paths = paths

  def __init__(self, port=9000):
    super().__init__(port)
    self.init_topo()

  def poll_counter(self, switch):
    def f():
      for port in [1,2,3,4]:
          self.counter_request(switch, "incoming", port)
          self.counter_request(switch, "outgoing", port)
      IOLoop.instance().call_later(delay=5, callback=f)
    f()

  def counter_response(self, switch, name, index, count):
    print(f"Count: {switch} {name}[{index}]={count}")

  def switch_up(self,switch,ports):
    host_map = { "h1" : { "ip" : "167772417", "mac" : "8796093022481" },
                 "h2" : { "ip" : "167772418", "mac" : "8796093022498" },
                 "h3" : { "ip" : "167772419", "mac" : "8796093022515" },
                 "h4" : { "ip" : "167772420", "mac" : "8796093022532" } }
    print(f"{switch} is up with ports {ports}!")
    self.poll_counter(switch)
    for host in self.topo.hosts():
      next_hop = self.topo.shortest_path_next_hop(switch,host)
      port = str(self.topo.port(switch,next_hop))
      ip = host_map[host]["ip"]
      mac = host_map[host]["mac"]
      print(f"Host {host} via {port}")
      entry = Entry("ipv4", [("hdr.ipv4.dstAddr", ip)], "ipv4_forward", [("dstAddr", mac), ("port", port)])
      self.insert(switch, entry)
    return

app = MyApp()
app.start()
