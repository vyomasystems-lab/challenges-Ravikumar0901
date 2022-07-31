module BCD_adder(a,b,cin,sum,cout);
    input [3:0] a,b;
    input cin;
    output [3:0] sum;
    output cout;
    reg [4:0] temp;
    reg [3:0] sum;
    reg cout;  

    always @(a,b,cin)
    begin
        temp = a+b+cin; 
        if(temp > 9)    
	begin
            temp = temp+6; //add 6, if result is more than 9.
            cout = 1;  //set the carry output
            sum = temp[3:0];   
   	end
        else    
	begin
            cout = 0;
            sum = temp[3:0];
        end
    end     