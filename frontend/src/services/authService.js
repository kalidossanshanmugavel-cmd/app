import api from "../api/axios";

export async function login(username, password) {

    const form = new URLSearchParams();

    form.append("username", username);
    form.append("password", password);

    const response = await api.post(
        "/login",
        form,
        {
            headers: {
                "Content-Type":
                "application/x-www-form-urlencoded"
            }
        }
    );

    return response.data;
}


export async function logout() {

    const response = await api.post("/logout");

    return response.data;

}