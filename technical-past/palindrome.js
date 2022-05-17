/*Have the function PalindromeTwo(str) take the str parameter being passed and return the string true if the parameter is a palindrome, (the string is the same forward as it is backward) otherwise return the string false. The parameter entered may have punctuation and symbols but they should not affect whether the string is in fact a palindrome. For example: "Anne, I vote more cars race Rome-to-Vienna" should return true.*/

function allLetter(inputtxt){
  var reg = /[a-z]/i

  let inputArr = inputtxt.split('')
  let newArr = []

  for(letter of inputArr){
    if(reg.test(letter)){
      newArr.push(letter)
    }
  }

  let newInput = newArr.join('')
  let revNewInputArr = newArr.reverse()
  let revInput = revNewInputArr.join('')

  if ( newInput == revInput ){
    return true
  }
  return false

}

