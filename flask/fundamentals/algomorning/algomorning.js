// const arr1 = ["a", "a", "a"];
// const arr2 = ["a", "b", "a", "c", "B", "c", "c", "d"];
// const arr3 = [];


// function makeFrequencyTable(arr) {
//     var newDict = {};
//     var counter=0;
//     for (var i=0;i <= arr.length;i++){
//         var temp=arr[i];
//         for(var j=0;j<arr.length;j++){
//             if(arr[j]==temp){
//                 counter++
//             }
//         }
//         newDict[arr[i]]=counter;
//         counter=0;
        
    
//     }return newDict
// } 
// makeFrequencyTable(arr1);
// makeFrequencyTable(arr2);
// makeFrequencyTable(arr3);
// console.log(makeFrequencyTable(arr1));
// console.log(makeFrequencyTable(arr2));
// console.log(makeFrequencyTable(arr3));


const arr1 = ["a", "a", "a"];
const arr2 = ["a", "b", "a", "c", "B", "c", "c", "d"];
const arr3 = [];

function makeFrequencyTable(arr) {
    var freqTable = {};
    for(var str of arr){
        //for(var i = 0;i < arr.length; i++)
        if(!freqTable[str]){
            freqTable[str]= 1;
        } else {
            freqTable[str]++;
        }
    } 
    return freqTable
}

makeFrequencyTable(arr1);
makeFrequencyTable(arr2);
makeFrequencyTable(arr3);
console.log(makeFrequencyTable(arr1));
console.log(makeFrequencyTable(arr2));
console.log(makeFrequencyTable(arr3));




/*****************************************************************************/

// /* 
// Given a non-empty array of odd length containing ints where every int but one
// has a matching pair (another int that is the same)
// return the only int that has no matching pair.
// */

const nums1 = [1];
const nums2 = [5, 4, 5];
const nums3 = [5, 4, 3, 4, 3, 4, 5];
const nums4 = [5, 2, 6, 2, 3, 1, 6, 3, 2, 5, 2];


// function oddOccurrencesInArray(nums) {
//     if (nums.length == 1){
//         return arr
//     }
//     var notPair=[];
//     for (var i=0;i<nums.length;i++){
//         for(var j=0;j<nums.length;j++){
//             if (arr[i] == arr[j]) {

    function makeFrequencyTable(nums) {
        var freqTable= makeFrequencyTable(nums);
    
        for ( var key in freqTable){
            if (freqTable[key] % 2 != 0){
                return key
            }
        }
    }




console.log(oddOccurrencesInArray(nums1), "should equal", expected1);
console.log(oddOccurrencesInArray(nums2), "should equal", expected2);
console.log(oddOccurrencesInArray(nums3), "should equal", expected3);
console.log(oddOccurrencesInArray(nums4), "should equal", expected4);

