// // // // const arr1 = ["a", "a", "a"];
// // // // const arr2 = ["a", "b", "a", "c", "B", "c", "c", "d"];
// // // // const arr3 = [];


// // // // function makeFrequencyTable(arr) {
// // // //     var newDict = {};
// // // //     var counter=0;
// // // //     for (var i=0;i <= arr.length;i++){
// // // //         var temp=arr[i];
// // // //         for(var j=0;j<arr.length;j++){
// // // //             if(arr[j]==temp){
// // // //                 counter++
// // // //             }
// // // //         }
// // // //         newDict[arr[i]]=counter;
// // // //         counter=0;
        
    
// // // //     }return newDict
// // // // } 

// // // // makeFrequencyTable(arr1);
// // // // makeFrequencyTable(arr2);
// // // // makeFrequencyTable(arr3);
// // // // console.log(makeFrequencyTable(arr1));
// // // // console.log(makeFrequencyTable(arr2));
// // // // console.log(makeFrequencyTable(arr3));


// // // const arr1 = ["a", "a", "a"];
// // // const arr2 = ["a", "b", "a", "c", "B", "c", "c", "d"];
// // // const arr3 = [];

// // // function makeFrequencyTable(arr) {
// // //     var freqTable = {};
// // //     for(var str of arr){
// // //         //for(var i = 0;i < arr.length; i++)
// // //         if(!freqTable[str]){
// // //             freqTable[str]= 1;
// // //         } else {
// // //             freqTable[str]++;
// // //         }
// // //     } 
// // //     return freqTable
// // // }

// // // makeFrequencyTable(arr1);
// // // makeFrequencyTable(arr2);
// // // makeFrequencyTable(arr3);
// // // console.log(makeFrequencyTable(arr1));
// // // console.log(makeFrequencyTable(arr2));
// // // console.log(makeFrequencyTable(arr3));




// // // /*****************************************************************************/

// // // // /* 
// // // // Given a non-empty array of odd length containing ints where every int but one
// // // // has a matching pair (another int that is the same)
// // // // return the only int that has no matching pair.
// // // // */

// // // const nums1 = [1];
// // // const nums2 = [5, 4, 5];
// // // const nums3 = [5, 4, 3, 4, 3, 4, 5];
// // // const nums4 = [5, 2, 6, 2, 3, 1, 6, 3, 2, 5, 2];


// // // // function oddOccurrencesInArray(nums) {
// // // //     if (nums.length == 1){
// // // //         return arr
// // // //     }
// // // //     var notPair=[];
// // // //     for (var i=0;i<nums.length;i++){
// // // //         for(var j=0;j<nums.length;j++){
// // // //             if (arr[i] == arr[j]) {

// // //     function makeFrequencyTable(nums) {
// // //         var freqTable= makeFrequencyTable(nums);
    
// // //         for ( var key in freqTable){
// // //             if (freqTable[key] % 2 != 0){
// // //                 return key
// // //             }
// // //         }
// // //     }




// // // console.log(oddOccurrencesInArray(nums1), "should equal", expected1);
// // // console.log(oddOccurrencesInArray(nums2), "should equal", expected2);
// // // console.log(oddOccurrencesInArray(nums3), "should equal", expected3);
// // // console.log(oddOccurrencesInArray(nums4), "should equal", expected4);



// // /* 
// //   Given a string,
// //   return a new string with the duplicates excluded
// //   Bonus: Keep only the last instance of each character.
// // */

// // // const str1 = "abcABC";
// // // const str2 = "helloo";
// // // const str3 = "";
// // // const str4 = "aa";




// // // // /**
// // // //  * De-dupes the given string.
// // // //  * @param {string} str A string that may contain duplicates.
// // // //  * @returns {string} The given string with any duplicate characters removed.
// // // //  */

// // // function stringDepupe(str) {
// // //     var temp = "";
// // //     for(var i of str){
// // //         var match=false
// // //         for(var j of temp){
// // //             if(i==j){
// // //                 match = true
// // //             } 
// // //         }
// // //         if (match==false)
// // //         temp+=i
// // //     }console.group(temp)
// // // }

// // // stringDepupe(str1);
// // // stringDepupe(str2);
// // // stringDepupe(str3);
// // // stringDepupe(str4);
// // /*******************************/

// // // /* 
// // //   Given a string containing space separated words
// // //   Reverse each word in the string.
// // //   If you need to, use .split to start, then try to do it without.
// // // */

// // const str1 = "hello";
// // const expected1 = "olleh";

// // const str2 = "hello world";
// // const expected2 = "olleh dlrow";

// // const str3 = "abc def ghi";
// // const expected3 = "cba fed ihg";

// // // /**
// // //  * Reverses the letters in each words in the given space separated
// // //  * string of words. Does NOT reverse the order of the words themselves.
// // //  * @param {string} str Contains space separated words.
// // //  * @returns {string} The given string with each word's letters reversed.
// // //  */
// // function reverseWords(str) {
// //     temp=str.split(" ")
// //     var final =""
// //     for(var j=0; j<temp.length;j++){
// //         for(var i =temp.length-1;i>=0;i--){
// //         temp += str[i]
// //     }
// // }
// // reverseWords(str1);
// // reverseWords(str2);
// // reverseWords(str3);


// // /***********************************/

// // /* 
// //   Reverse Word Order
// //   Given a string of words (with spaces)
// //   return a new string with words in reverse sequence.
// // */

// const str1 = "This is a test";
// const expected1 = "test a is This";

// const str2 = "hello";
// const expected2 = "hello";

// const str3 = "   This  is a   test  ";
// const expected3 = "test a is This";

// // /**
// //  * Reverses the order of the words but not the words themselves form the given
// //  * string of space separated words.
// //  * @param {string} wordsStr A string containing space separated words.
// //  * @returns {string} The given string with the word order reversed but the words
// //  *    themselves are not reversed.
// //  */
// function reverseWordOrder(wordsStr) {
//     var temp=wordsStr.split(" ")
//     var final=""
//     for (var j=temp.length-1;j>=0;j--){
//         final += temp[j]
//         final += " "
//     }console.log(final)
// }
// reverseWordOrder(str1);
// reverseWordOrder(str2);
// reverseWordOrder(str3);



/* 
Parens Valid
Given an str that has parenthesis in it
return whether the parenthesis are valid
*/

// const str1 = "Y(3(p)p(3)r)s";
// const expect1 = true;

// const str2 = "N(0(p)3";
// const expect2 = false;
// // Explanation: not every parenthesis is closed.

// const str3 = "N(0)t ) 0(k";
// const expect3 = false;
// // Explanation: because the second ")" is premature: there is nothing open for it to close.

// const str4 = "a(b))(c";
// const expect4 = false;
// // Explanation: same number of opens and closes but the 2nd closing closes nothing.

// /**
//  * Determines whether the parenthesis in the given string are valid.
//  * Each opening parenthesis must have exactly one closing parenthesis.
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {string} str
//  * @returns {boolean} Whether the parenthesis are valid.
//  */
// function parensValid(str) {
//     var counter=0;
//     var counter1=0;
//     for (var char of str){
//         if (char == "("){
//             counter++;
//             console.log("Opening: " + counter)
//         } else if(char==")"){
//             counter1++;
//             console.log("Closing: " + counter1)
//         } if(counter1 > counter){
//             return false
        
//         }
//     } 
//     if (counter == counter1){
//         return true;
//     } else{
//         return false;
//     }
// }
// console.log(parensValid(str1));
// console.log(parensValid(str2));
// console.log(parensValid(str3));
// console.log(parensValid(str4));


/*****************************************************************************/

/* 
Braces Valid
Given a string sequence of parentheses, braces and brackets, determine whether it is valid. 
*/

const str1a = "W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!";
const expected1 = true;

const str2a = "D(i{a}l[ t]o)n{e";
const expected2 = false;

const str3a = "A(1)s[O (n]0{t) 0}k";
const expected3 = false;
```
/**
 * Determines whether the string's braces, brackets, and parenthesis are valid
 * based on the order and amount of opening and closing pairs.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the given strings braces are valid.
 */
// function bracesValid(str) {
//     var opening = 0;
//     var closing = 0;
    
//     for (var char of str){
//         if(char == "(" || char =="[" || char == "{"){
//             opening++;
//             console.log("Opening: " + opening);
//         }else if(char == ")" || char== "]" || char=="}"){
//             closing++;
//             console.log("Closing")
//         }   
//         if(closing > opening){
//             return false
//         }
//     }
//     if (opening == closing){
//         return true;
//     } else{
//         return false;
//     }
// }

// console.log(bracesValid(str1a));
// console.log(bracesValid(str2a));
// console.log(bracesValid(str3a));

function bracesValid(str) {
    var openingP = 0;
    var closingP = 0;
    var openingS = 0;
    var closingS = 0;
    var openingB = 0;
    var closingB = 0;
    
    for(var char of str){
        
    }
