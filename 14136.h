#include <string.h>
//implement split string function, return 2d char array to store result, set correct number of splitted strings

int size = 1000;

int check(char*string, char*pattern){
    int patternLen = strlen(pattern);
    for(int i = 0; i < patternLen; i++){
        if(*(string + i) == *(pattern + i)){
            continue;
        }
        else{
            return 0;
        }
    }
    return 1;
}

char **split(char* string, char* pattern, int* splittedStrings){
    int patternLen = strlen(pattern);
    int stringLen = strlen(string);
    int i = 0;
    while(i < stringLen){
        int res = check(&string[i], pattern);
        if(res){
            int j = i;
            while(i < j + patternLen){
                string[i] = '!';
                i++;
            }
            i--;
        }
        i++;
    }
    //printf("%s\n", string);
    //--> i!!!am!!!luffy

    // bikin ke result
    char ** result = malloc(size * sizeof(char*));
    for(int i = 0; i < size; i++){
        result[i] = malloc((stringLen + 1) * sizeof(char));
    }

    // Masukin
    int resultIdx = 0;
    int idxDalam = 0;
    int startingIdx = 0;
    i = 0;
    // handle '!' di awal
    if(string[i] == '!'){
        while(string[i] == '!'){
            i++;
        }
    }
    while(i < stringLen){
        result[resultIdx][idxDalam] = string[i];
        idxDalam++;
        i++;
        if(string[i] == '!' || string[i] == '\0'){
            result[resultIdx][idxDalam] = '\0';
            idxDalam = 0;
            resultIdx++;
            *splittedStrings = *splittedStrings + 1;
            while(string[i] == '!'){
                i++;
            }
        }
    }


    return result;
}
//free memory space
void free_(char **result, int splittedStrings){
    for(int i =0; i < size; i++){
        free(result[i]);
    }
    free(result);
}
