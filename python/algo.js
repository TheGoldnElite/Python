function array(arr){
    if(arr.length <=2){
        return -1;
    }
}
    for (var i = 0;i<arr.length;i++){
        //i represents the index of a given array item
        for (var j=0;j<arr.length;j++){
            var leftItems =0;
            var rightItems=0;
            if (j < 1){
                leftItems += arr[j];
            }
            else if(j>i){
                rightItems += arr[j];
            }
        }
        if (leftItems ==rightItems){
            return i;
        }
    }
    return -1
