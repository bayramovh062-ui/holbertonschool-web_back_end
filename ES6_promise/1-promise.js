export const getFullResponseFromAPI = (flag) => {
  return new Promise((resolve, reject) => {
    if(flag) {
      resolve({status: 200, body: "Succes"})
    }else {
      reject("The fake API is not working currently")
    }
  })
}

export default getFullResponseFromAPI