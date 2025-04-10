import p4runtime_sh.shell as sh

# Note: 9559 is the default TCP port number on which the
# simple_switch_grpc process is listening for incoming TCP connections,
# over which a client program can send P4Runtime API messages to
# simple_switch_grpc.
my_dev1_addr = "localhost:9559"
my_dev1_id = 0
p4info_txt_fname = "./build/demo.p4info.txtpb"
p4prog_binary_fname = "./build/demo.json"

sh.setup(device_id = my_dev1_id,
         grpc_addr = my_dev1_addr,
         election_id = (0, 1),              # (high_32bits, lo_32bits)
         config = sh.FwdPipeConfig(p4info_txt_fname, p4prog_binary_fname))

def add_l2_lpm_entry_action_l2_forward(match_addr_str, new_addr_str, port):
    te = sh.TableEntry("l2_lpm")(action="l2_forward")

    te.match["ethernet.dstAddr"] = match_addr_str
    te.action["dstAddr"] = new_addr_str
    te.action["port"] = "%d" % (port)
    te.insert()

add_l2_lpm_entry_action_l2_forward("02:02:02:ef:ef:ef", "02:02:02:ff:ff:ff", 2)
add_l2_lpm_entry_action_l2_forward("03:03:03:ef:ef:ef", "03:03:03:ff:ff:ff", 3)