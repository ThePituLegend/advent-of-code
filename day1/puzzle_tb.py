import random
import cocotb
from cocotb.triggers import RisingEdge, FallingEdge, ClockCycles, Timer
from cocotb.clock import Clock

@cocotb.test()
async def test_puzzle(dut):

    input_file = open("input.txt", "r")

    dut.clk_i.value = 0;
    dut.rstn_i.value = 1;
    dut.run_i.value = 0;
    dut.char_i.value = 0;

    cocotb.start_soon(Clock(dut.clk_i, 1, units="ns").start())  # run the clock "in the background"

    # Reset
    await RisingEdge(dut.clk_i)
    dut.rstn_i.value = 0;
    await ClockCycles(dut.clk_i, 2) # Hold reset for 2 clock cycles
    dut.rstn_i.value = 1;

    # Start processing
    dut.run_i.value = 1;
    for line in input_file:
        for char in line:
            await RisingEdge(dut.clk_i)
            dut.char_i.value = ord(char);

    # Stop processing
    await RisingEdge(dut.clk_i)
    dut.run_i.value = 0;

    await Timer(5, units="ns") # Wait a bit, just for the looks of the waveform

    print(f"Puzzle Result: {int(dut.sum_o.value)}")

    input_file.close()
