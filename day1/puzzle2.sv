/*
 * Advent of Code 2023 - Day 1
 * Puzzle 2
 *
 * From a list of strings, find the first and last digits to compose a two-digit number.
 * Those digits could either be written as a digit (as is) or spelled out (e.g. "one").
 * Sum all the numbers that can be composed from the list.
*/

`timescale 1us/1ns

module shift_reg
(
    input logic clk_i,
    input logic rstn_i,
    input logic enable_i,
    input logic [7:0] data_i,
    output logic [4:0][7:0] data_o
);

always_ff @(posedge clk_i or negedge rstn_i) begin
    if (!rstn_i) begin
        data_o <= '0;
    end else begin
        if (enable_i) begin
            for (int i = 1; i < 5; i++) begin
                data_o[i] <= data_o[i-1];
            end
            data_o[0] <= data_i;
        end
    end
end
endmodule

// Function to check if a window contains a valid spelling
function logic [3:0] check_spelling (logic [4:0][7:0] window);
    if (window[3:0] == "zero") begin
        return 0;
    end else if (window[2:0] == "one") begin
        return 1;
    end else if (window[2:0] == "two") begin
        return 2;
    end else if (window[4:0] == "three") begin
        return 3;
    end else if (window[3:0] == "four") begin
        return 4;
    end else if (window[3:0] == "five") begin
        return 5;
    end else if (window[2:0] == "six") begin
        return 6;
    end else if (window[4:0] == "seven") begin
        return 7;
    end else if (window[4:0] == "eight") begin
        return 8;
    end else if (window[3:0] == "nine") begin
        return 9;
    end else begin
        return 10; // Invalid spelling
    end
endfunction

module puzzle2
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
logic [3:0] spell2num;
state_t state, next_state;
logic newline;

logic [4:0][7:0] window;

// Shift register
shift_reg shift_reg_inst (
    .clk_i(clk_i),
    .rstn_i(rstn_i && !newline),
    .enable_i(run_i && !newline),
    .data_i(char_i),
    .data_o(window)
);

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
            spell2num = '0;
            newline = 0;
            if (run_i) begin
                next_state = FIRST;
            end
        end
        FIRST:
        begin
            newline = 0;
            spell2num = check_spelling(window); // check spelling
            if (spell2num < 10) begin
                tens = spell2num * 7'd10;
                next_state = SECOND;
            end else if (char_i >= "0" && char_i <= "9") begin // check digit
                tens = 4'(char_i - "0") * 7'd10; // char_i -> 10's digit
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
            end else begin
                spell2num = check_spelling(window); // check spelling
                if (spell2num < 10) begin
                    units = spell2num;
                end
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