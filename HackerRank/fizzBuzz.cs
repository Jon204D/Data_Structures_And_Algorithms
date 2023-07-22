/*
 * Given a number n, for each integer i in the range from 1 to n inclusive, print one
 * value per line as follows:
 * if i is a multiple of both 3 and 5, print "FizzBuzz"
 * if i is a multiple of 3, print "Fizz"
 * if i is a multiple of 5, print "Buzz"
 * if i is not a multiple of 3 or 5, print the value of i.
 */

using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Collections;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using System.Text.RegularExpressions;
using System.Text;
using System;



class Result
{

    /*
     * Complete the 'fizzBuzz' function below.
     *
     * The function accepts INTEGER n as parameter.
     */

    public static void fizzBuzz(int n)
    {
        for (int i = 1; i <= n; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                Console.WriteLine("FizzBuzz");
            }
            else if (i % 3 == 0){
                Console.WriteLine("Fizz");
            }
            else if (i % 5 == 0) {
                Console.WriteLine("Buzz");
            }
            else {
                Console.WriteLine(i);
            }
        }
    }

}

class Solution
{
    public static void Main(string[] args)
    {
        int n = Convert.ToInt32(Console.ReadLine().Trim());

        Result.fizzBuzz(n);
    }
}