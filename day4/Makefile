# Makefile

# defaults
SIM ?= verilator
EXTRA_ARGS += --trace-fst --trace-structs
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += $(PWD)/puzzle1.sv
VERILOG_SOURCES += $(PWD)/puzzle2.sv

MODULE = puzzle_tb

# include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim