BUILD_DIR = build
PCAP_DIR = 
LOG_DIR = 

P4C = p4c
P4C_ARGS += --target bmv2 --arch v1model --p4runtime-files $(BUILD_DIR)/$(basename $@).p4info.txtpb

BMV2_SWITCH = simple_switch_grpc
SWITCH_ARGS = --log-console --dump-packet-data 10000 --no-p4

source = demo.p4
compiled_json := $(source:.p4=.json)

all: build

run:
	$(BMV2_SWITCH) $(SWITCH_ARGS) -i 0@veth0 -i 1@veth2 -i 2@veth4 -i 3@veth6 -i 4@veth8 -i 5@veth10 -i 6@veth12 -i 7@veth14


build: dirs $(compiled_json)

%.json: %.p4
	$(P4C) $(P4C_ARGS) -o $(BUILD_DIR) $<

dirs:
	mkdir -p $(BUILD_DIR) $(PCAP_DIR) $(LOG_DIR)

clean:
	rm -f *.pcap
	rm -rf $(BUILD_DIR) $(PCAP_DIR) $(LOG_DIR)
