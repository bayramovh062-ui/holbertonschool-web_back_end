import signUpUser from "./4-user-promise";
import uploadPhoto from "./5-photo-reject";

export default function handleProfileSignup(firstName, lastName, fileName) {
  return [
    {
        status: signUpUser().status,
        value: signUpUser().value
    },
    {
        status: uploadPhoto.status,
        value: uploadPhoto.value
    }
  ]
}