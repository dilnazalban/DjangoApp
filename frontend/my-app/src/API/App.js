import axios from "axios";

export async function categoryList() {
    try {
        const response = await axios.get("http://127.0.0.1:8000/api/v1/categories/", )
        return response.data
    } catch (e) {
        return null
    }
}
export async function appList() {
    try {
        const response = await axios.get("http://127.0.0.1:8000/api/v1/apps/", )
        return response.data
    } catch (e) {
        return null
    }
}