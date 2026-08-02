export const getFullResponseFromAPI = (succes) => {
  return new Promise((resolve, reject) => {
    if(succes) {
      resolve({status: 200, body: "Succes"})
    }else {
      reject("The fake API is not working currently")
    }
  })
}

export default getFullResponseFromAPI