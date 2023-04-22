import axios from "axios";



export async function loginAPI(username, password) {
    try {
        const response = await axios.post("http://127.0.0.1:8000/api/v1/login/", {
            username: username,
            password: password
        })
        return response.data
    } catch (e) {
        return null
    }
}
export async function registerUser(username, password1,password2, email ) {
    try {
        const response = await axios.post("http://127.0.0.1:8000/api/v1/register/", {
            username: username,
            password1: password1,
            password2: password2,
            email: email,
        })
        return response.data
    } catch (e) {
        return null
    }
}
export async function logoutAPI(){
    try {
       const response = await axios.post("http://127.0.0.1:8000/api/v1/logout/")
        return response.data
    }catch (e) {
        console.log("error")
    }
}

