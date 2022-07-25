# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    """Test for input as 1101 """
    S=1100
    #input Driving
    dut.sel.value = S

    await Timer(2,units='2')
    assert dut.out.value == inp12,f"Mux Result is incorrect: {dut.X.value}!=12"


    