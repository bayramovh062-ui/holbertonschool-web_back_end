import signUpUser from "./4-user-promise";
import uploadPhoto from "./5-photo-reject";

export default function handleProfileSignup(firstName, lastName, fileName) {
  return [
    {
        status: signUpUser(firstName, lastName).status,
        value: signUpUser(firstName, lastName).value
    },
    {
        status: uploadPhoto(fileName).status,
        value: uploadPhoto(fileName).value
    }
  ]
}