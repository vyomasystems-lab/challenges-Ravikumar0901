# See LICENSE.cocotb for details
# See LICENSE.vyoma for details

# Simple tests for an adder module
import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def adder_basic_test(dut):
    """Test for 5 + 3"""

    A = 9
    B = 6
    Cin=0
    Co=1

    # input driving
    dut.a.value = A
    dut.b.value = B
    dut.cin.value = Cin

    dut.cout.value = Co


    await Timer(2, units='ns')

    assert dut.sum.value == Co"+"A+B+Cin,f"Adder result is incorrect: {dut.sum.value} != 5"
    