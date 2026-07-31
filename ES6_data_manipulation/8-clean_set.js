export default function cleanSet(set, startString) {
    if(startString === ''){
        return ''
    }
  let result = ''
  for (let value of set){
    if(value.startsWith(startString)){
      result += value.slice(startString.length, value.length) + '-'
    }
  }
  return result.slice(0, result.length -1)
}