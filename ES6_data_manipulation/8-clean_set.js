export default function cleanSet(set, startString) {
    let result = ''
  for (let value of set){
    if(value.startsWith(startString)){
        result += value.splice(0, startString.length) + '-'
    }
  }
}