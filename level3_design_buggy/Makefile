# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)

VERILOG_SOURCES = $(PWD)/BCD_Adder_bug.v              # provide your design path

TOPLEVEL := BCD_Adder_bug        # design file
MODULE   := test_BCD_Adder_bug     # test file

include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all: clean
	rm -rf *.xml sim_build __pycache__ 
