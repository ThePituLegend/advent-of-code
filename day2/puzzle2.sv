/*
 * Advent of Code 2023 - Day 2
 * Puzzle 2
 *
 * The module will receive each cycle the RGB cubes extracted from a bag, from different games.
 * It will keep track of the largest cube value for each color, and when instructed to go to the next game,
 * it will determine the game power (the product of the largest cube value for each color).
 * When the process is finished, it will output the sum of the powers.
*/

`timescale 1us/1ns

module puzzle2
(
    input logic clk_i,
    input logic rstn_i,
    input logic run_i,
    input logic new_game_i,
    input logic [31:0] red_cubes_i,
    input logic [31:0] green_cubes_i,
    input logic [31:0] blue_cubes_i,
    output logic [31:0] sum_o
);

logic [31:0] red_max;
logic [31:0] green_max;
logic [31:0] blue_max;

logic [31:0] sum;

// Keep track of the largest cube value for each color
always_ff @(posedge clk_i or negedge rstn_i) begin
    if (!rstn_i) begin
        red_max     <= '0;
        green_max   <= '0;
        blue_max    <= '0;
    end else if (run_i) begin
        if (new_game_i) begin
            red_max     <= '0;
            green_max   <= '0;
            blue_max    <= '0;
        end else begin
            red_max     <= (red_cubes_i   > red_max)   ? red_cubes_i    : red_max;
            green_max   <= (green_cubes_i > green_max) ?  green_cubes_i : green_max;
            blue_max    <= (blue_cubes_i  > blue_max)  ? blue_cubes_i   : blue_max;
        end
    end
end

// Determine the power and add it to the sum
always_ff @(posedge clk_i or negedge rstn_i) begin
    if (!rstn_i) begin
        sum <= '0;
    end else if (run_i) begin
        if (new_game_i) begin
            sum <= sum + red_max * green_max * blue_max;
        end
    end
end

// Output the sum of the valid games' IDs
always_ff @(posedge clk_i or negedge rstn_i) begin
    if (!rstn_i) begin
        sum_o <= '0;
    end else if (!run_i) begin
        sum_o <= sum;
    end
end

endmodule