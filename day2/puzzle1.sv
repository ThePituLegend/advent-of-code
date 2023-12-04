/*
 * Advent of Code 2023 - Day 2
 * Puzzle 1
 *
 * The module will receive each cycle the RGB cubes extracted from a bag, from different games.
 * It will keep track of the largest cube value for each color, and when instructed to go to the next game,
 * it will determine if the game is valid or not.
 * When the process is finished, it will output the sum of the valid games' IDs.
*/

`timescale 1us/1ns

module puzzle1
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

localparam RED_CAP = 12;
localparam GREEN_CAP = 13;
localparam BLUE_CAP = 14;

logic [31:0] red_max;
logic [31:0] green_max;
logic [31:0] blue_max;

logic [31:0] current_id;

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

// Determine if the game is valid or not
always_ff @(posedge clk_i or negedge rstn_i) begin
    if (!rstn_i) begin
        sum <= '0;
        current_id <= '0;
    end else if (run_i) begin
        if (new_game_i) begin
            if (red_max <= RED_CAP && green_max <= GREEN_CAP && blue_max <= BLUE_CAP) begin
                sum <= sum + current_id;
            end
            current_id <= current_id + 1;
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