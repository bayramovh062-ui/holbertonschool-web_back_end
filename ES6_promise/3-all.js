import { uploadPhoto, createUser } from './utils'

export default function handleProfileSignup() {

  const uploadPromise = uploadPhoto()
  const createPromise = createUser()

  return Promise.all([uploadPromise, createPromise])
  .then(([photo, user]) => console.log(`${photo.body} ${user.firstName} ${user.lastName}`))
  .catch(()=> console.log("Signup system offline"))
}