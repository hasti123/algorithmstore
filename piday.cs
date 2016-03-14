using System;
using System.Collections.Generic;
using System.Linq;

namespace PiDay
{
    class Program
    {
        public static void Main()
        {
            var numList = new List<char>();
            numList.Add('0');
            numList.Add('1');
            numList.Add('2');
            numList.Add('3');
            numList.Add('4');
            numList.Add('5');
            numList.Add('6');
            numList.Add('7');
            numList.Add('8');
            numList.Add('9');

            var perms = GeneratePermutations<char>(numList);
            var finalpermlist = new List<string>();
            foreach (var perm in perms)
            {
                var newPermutation = string.Join(",", perm.ToArray());
                
                finalpermlist.Add(newPermutation.Replace(",", ""));
            }

            foreach (var combination in finalpermlist)
            {
                var temp = Works(combination);
                if (temp)
                {
                    Console.WriteLine(combination);
                    Console.WriteLine("success");
                    Console.ReadKey();
                }
            }

            Console.WriteLine("Failure");
            Console.ReadKey();
        }

        private static long BuildNextNumber(string num, int numberSize)
        {
            return long.Parse(num.Substring(0, numberSize));
        }

        private static bool Works(string num)
        {
            for (int i = 1; i <= 10; i++)
            {
                var tempNum = BuildNextNumber(num, i);
                if (tempNum % i != 0)
                {
                    return false;
                }
            }

            return true;
        }

        private static List<List<T>> GeneratePermutations<T>(List<T> items)
        {
            // Make an array to hold the
            // permutation we are building.
            T[] current_permutation = new T[items.Count];

            // Make an array to tell whether
            // an item is in the current selection.
            bool[] in_selection = new bool[items.Count];

            // Make a result list.
            List<List<T>> results = new List<List<T>>();

            // Build the combinations recursively.
            PermuteItems<T>(items, in_selection,
                current_permutation, results, 0);

            // Return the results.
            return results;
        }

        // Recursively permute the items that are
        // not yet in the current selection.
        private static void PermuteItems<T>(List<T> items, bool[] in_selection, T[] current_permutation, List<List<T>> results, int next_position)
        {
            // See if all of the positions are filled.
            if (next_position == items.Count)
            {
                // All of the positioned are filled.
                // Save this permutation.
                results.Add(current_permutation.ToList());
            }
            else
            {
                // Try options for the next position.
                for (int i = 0; i < items.Count; i++)
                {
                    if (!in_selection[i])
                    {
                        // Add this item to the current permutation.
                        in_selection[i] = true;
                        current_permutation[next_position] = items[i];

                        // Recursively fill the remaining positions.
                        PermuteItems<T>(items, in_selection,
                            current_permutation, results,
                            next_position + 1);

                        // Remove the item from the current permutation.
                        in_selection[i] = false;
                    }
                }
            }
        }
    }
}
