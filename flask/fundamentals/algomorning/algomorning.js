// // // const arr1 = ["a", "a", "a"];
// // // const arr2 = ["a", "b", "a", "c", "B", "c", "c", "d"];
// // // const arr3 = [];


// // // function makeFrequencyTable(arr) {
// // //     var newDict = {};
// // //     var counter=0;
// // //     for (var i=0;i <= arr.length;i++){
// // //         var temp=arr[i];
// // //         for(var j=0;j<arr.length;j++){
// // //             if(arr[j]==temp){
// // //                 counter++
// // //             }
// // //         }
// // //         newDict[arr[i]]=counter;
// // //         counter=0;
        
    
// // //     }return newDict
// // // } 

// // // makeFrequencyTable(arr1);
// // // makeFrequencyTable(arr2);
// // // makeFrequencyTable(arr3);
// // // console.log(makeFrequencyTable(arr1));
// // // console.log(makeFrequencyTable(arr2));
// // // console.log(makeFrequencyTable(arr3));


// // const arr1 = ["a", "a", "a"];
// // const arr2 = ["a", "b", "a", "c", "B", "c", "c", "d"];
// // const arr3 = [];

// // function makeFrequencyTable(arr) {
// //     var freqTable = {};
// //     for(var str of arr){
// //         //for(var i = 0;i < arr.length; i++)
// //         if(!freqTable[str]){
// //             freqTable[str]= 1;
// //         } else {
// //             freqTable[str]++;
// //         }
// //     } 
// //     return freqTable
// // }

// // makeFrequencyTable(arr1);
// // makeFrequencyTable(arr2);
// // makeFrequencyTable(arr3);
// // console.log(makeFrequencyTable(arr1));
// // console.log(makeFrequencyTable(arr2));
// // console.log(makeFrequencyTable(arr3));




// // /*****************************************************************************/

// // // /* 
// // // Given a non-empty array of odd length containing ints where every int but one
// // // has a matching pair (another int that is the same)
// // // return the only int that has no matching pair.
// // // */

// // const nums1 = [1];
// // const nums2 = [5, 4, 5];
// // const nums3 = [5, 4, 3, 4, 3, 4, 5];
// // const nums4 = [5, 2, 6, 2, 3, 1, 6, 3, 2, 5, 2];


// // // function oddOccurrencesInArray(nums) {
// // //     if (nums.length == 1){
// // //         return arr
// // //     }
// // //     var notPair=[];
// // //     for (var i=0;i<nums.length;i++){
// // //         for(var j=0;j<nums.length;j++){
// // //             if (arr[i] == arr[j]) {

// //     function makeFrequencyTable(nums) {
// //         var freqTable= makeFrequencyTable(nums);
    
// //         for ( var key in freqTable){
// //             if (freqTable[key] % 2 != 0){
// //                 return key
// //             }
// //         }
// //     }




// // console.log(oddOccurrencesInArray(nums1), "should equal", expected1);
// // console.log(oddOccurrencesInArray(nums2), "should equal", expected2);
// // console.log(oddOccurrencesInArray(nums3), "should equal", expected3);
// // console.log(oddOccurrencesInArray(nums4), "should equal", expected4);



// /* 
//   Given a string,
//   return a new string with the duplicates excluded
//   Bonus: Keep only the last instance of each character.
// */

// // const str1 = "abcABC";
// // const str2 = "helloo";
// // const str3 = "";
// // const str4 = "aa";




// // // /**
// // //  * De-dupes the given string.
// // //  * @param {string} str A string that may contain duplicates.
// // //  * @returns {string} The given string with any duplicate characters removed.
// // //  */

// // function stringDepupe(str) {
// //     var temp = "";
// //     for(var i of str){
// //         var match=false
// //         for(var j of temp){
// //             if(i==j){
// //                 match = true
// //             } 
// //         }
// //         if (match==false)
// //         temp+=i
// //     }console.group(temp)
// // }

// // stringDepupe(str1);
// // stringDepupe(str2);
// // stringDepupe(str3);
// // stringDepupe(str4);
// /*******************************/

// // /* 
// //   Given a string containing space separated words
// //   Reverse each word in the string.
// //   If you need to, use .split to start, then try to do it without.
// // */

// const str1 = "hello";
// const expected1 = "olleh";

// const str2 = "hello world";
// const expected2 = "olleh dlrow";

// const str3 = "abc def ghi";
// const expected3 = "cba fed ihg";

// // /**
// //  * Reverses the letters in each words in the given space separated
// //  * string of words. Does NOT reverse the order of the words themselves.
// //  * @param {string} str Contains space separated words.
// //  * @returns {string} The given string with each word's letters reversed.
// //  */
// function reverseWords(str) {
//     temp=str.split(" ")
//     var final =""
//     for(var j=0; j<temp.length;j++){
//         for(var i =temp.length-1;i>=0;i--){
//         temp += str[i]
//     }
// }
// reverseWords(str1);
// reverseWords(str2);
// reverseWords(str3);


// /***********************************/

// /* 
//   Reverse Word Order
//   Given a string of words (with spaces)
//   return a new string with words in reverse sequence.
// */

const str1 = "This is a test";
const expected1 = "test a is This";

const str2 = "hello";
const expected2 = "hello";

const str3 = "   This  is a   test  ";
const expected3 = "test a is This";

// /**
//  * Reverses the order of the words but not the words themselves form the given
//  * string of space separated words.
//  * @param {string} wordsStr A string containing space separated words.
//  * @returns {string} The given string with the word order reversed but the words
//  *    themselves are not reversed.
//  */
function reverseWordOrder(wordsStr) {
    var temp=wordsStr.split(" ")
    var final=""
    for (var j=temp.length-1;j>=0;j--){
        final += temp[j]
        final += " "
    }console.log(final)
}
reverseWordOrder(str1);
reverseWordOrder(str2);
reverseWordOrder(str3);

