# See LICENSE.cocotb for details
# See LICENSE.vyoma for details

# Simple tests for an adder module
import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def adder_basic_test(dut):
    """Test for 5 + 3"""

    A = 5
    B = 3
    Cin=0

    # input driving
    dut.a.value = A
    dut.b.value = B
    dut.cin.value = Cin



    await Timer(2, units='ns')

    assert dut.sum.value == A+B+Cin,f"adder result was incorrect {dut.X.value}!=8"