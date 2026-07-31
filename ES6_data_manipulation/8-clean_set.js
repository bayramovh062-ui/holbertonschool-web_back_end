export default function cleanSet(set, startString) {
  let result = ''
  for (let value of set){
    if(value.startsWith(startString)){
      result += value.slice(startString.length -1, value.length) + '-'
    }
    return result.slice(0, result.length -1)
  }
}