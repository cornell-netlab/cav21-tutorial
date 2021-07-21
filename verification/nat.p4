/* Headers and Instances */
header_type ethernet_t {
 fields {
  dst_addr:48;
  src_addr:48;
  ether_type:16;
 }
}
header_type ipv4_t {
 fields {
  pre_ttl:64;
  ttl:8;
  protocol:8;
  checksum:16;
  src_addr:32;
  dst_addr:32;
 }
}
header ethernet_t ethernet;
header ipv4_t ipv4;

/* Parsers */
parser start {
  extract(ethernet);
  return select(ethernet.ether_type) {
    0x800: parse_ipv4;
    default: ingress;
  }
}
parser parse_ipv4 {
  extract(ipv4);
  return ingress;
}

/* Actions */
action allow() { 
 modify_field(standard_metadata.egress_spec,1);
}     
action deny() { drop(); }
action nop() { }     
action rewrite(dst_addr) {
  modify_field(ipv4.dst_addr,dst_addr);
}

/* Tables */
table acl {
 reads {
  ipv4.src_addr:lpm;
  ipv4.dst_addr:lpm;
 }
 actions { allow; deny; }
}

table nat {
  reads { ipv4.dst_addr:lpm; }
  actions { rewrite; nop; }
  default_action: nop();
}
    
/* Controls */
control ingress {
  //@pragma assume valid(ipv4)
  @pragma assume ipv4.dst_addr == H
  apply(acl);
  apply(nat);
  @pragma assert H == 10.0.1.1 implies drop
}

control egress { }
