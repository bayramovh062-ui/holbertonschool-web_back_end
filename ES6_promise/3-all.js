import { uploadPhoto, createUser } from './utils'

export default function handleProfileSignup() {
  const uploadPromise = uploadPhoto()
  const createPromise = createUser()
  Promise.all([uploadPromise, createPromise])
  .then(() => console.log(`${uploadPromise.body} ${createPromise.firstName} ${createPromise.lastName}`))
  .catch(()=> console.log("Signup system offline"))
}