import { useState } from "react"
import userServices from "../services/userServices"
import useGlobalReducer from "../hooks/useGlobalReducer"

export const Login = () => {
    const { store, dispatch } = useGlobalReducer()
    const [formData, setFormData] = useState({
        email: "",
        password: ""
    })

    const handleChange = e => {
        setFormData({ ...formData, [e.target.name]: e.target.value })
    }

    const handleSubmit = e => {
        e.preventDefault();
        console.log(formData)
        // userServices.login(formData).then(data => dispatch({ type: 'login_register', payload: data }))
        userServices.login(formData).then(data => console.log(data ))
    }

    return (
        <form onSubmit={handleSubmit}>
            <h2>Login</h2>
            <input placeholder="email" name="email" value={FormData.email} onChange={handleChange} type="email" />
            <input placeholder="password" name="password" value={FormData.password} onChange={handleChange} type="password" />
            <input type="submit" />
        </form>
    )
}