<?php
interface AdvancedArithmetic{
    public function divisorSum($n);
}
//Write your code here
class Calculator implements AdvancedArithmetic
{
    protected $stack;
    public function divisorSum($var)
    {
        $this->stack = array();
        for ($i = 1; $i <= $var; $i++) {
            if ($var % $i == 0) {
                //echo "value: " . $i ;
                array_unshift ($this->stack, $i);
            }
        }
        $total = 0;
        while (count($this->stack) > 0) {
            $total = $total + array_shift($this->stack);
        }
        //echo "TOTAL: " . $total;
        return $total;
    }
    
    
}



$n=intval(fgets(STDIN));
$myCalculator=new Calculator();
if($myCalculator instanceof AdvancedArithmetic)//checking if Calculator has implemented AdvancedArithemtic
{
    $sum=$myCalculator->divisorSum($n);
    echo "I implemented: AdvancedArithmetic\n".$sum;
}
else
{
    echo "Wrong answer";// You will get this output if you dont implement
}
?>