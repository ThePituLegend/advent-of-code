/*
 * Advent of Code 2023 - Day 1
 * Puzzle 1
 *
 * From a list of strings, find the first and last digits to compose a two-digit number.
 * Sum all the numbers that can be composed from the list.
*/

`timescale 1us/1ns

module puzzle1
    import commons::*;
(
    input logic clk_i,
    input logic rstn_i,
    input logic run_i,
    input logic [7:0] char_i,
    output logic [31:0] sum_o
);

logic [6:0] tens;
logic [3:0] units;
logic [31:0] sum;
state_t state, next_state;
logic newline;

// State machine
always_ff@(posedge clk_i, negedge rstn_i)
begin
    if (!rstn_i)
    begin
        state <= IDLE;
    end else
    begin
        state <= next_state;
    end
end

// State machine logic
always_comb
begin
    next_state = state;
    case (state)
        IDLE:
        begin
            tens = '0;
            units = '0;
            newline = 0;
            if (run_i) begin
                next_state = FIRST;
            end
        end
        FIRST:
        begin
            newline = 0;
            if (char_i >= "0" && char_i <= "9") begin
                tens = 7'(char_i - "0") * 7'd10; // char_i -> 10's digit
                next_state = SECOND;
            end
        end
        SECOND:
        begin
            if (!run_i) begin
                newline = 1; // End of run, as if a newline was found
                next_state = IDLE;
            end else if (char_i == "\n") begin
                newline = 1;
                next_state = FIRST;
            end else if (char_i >= "0" && char_i <= "9") begin
                units = 4'(char_i - "0"); // char_i -> 1's digit
            end
        end
        default:
        begin
            $error("ERROR: Invalid state");
        end
    endcase
end

// Sum output
always_ff @(posedge clk_i, negedge rstn_i)
begin
    if (!rstn_i)
    begin
        sum_o <= '0;
    end else if (state == IDLE)
    begin
        sum_o <= sum;
    end else if (state == SECOND && newline)
    begin
        sum <= sum + 32'(tens) + 32'(units);
    end
end

endmodule