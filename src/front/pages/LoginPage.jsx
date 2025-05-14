import { Link } from "react-router-dom"
import { Login } from "../components/login"

export const LoginPage = () => {

    return (
        <>
        <Login/>
        {/* Si no tenemos cuenta, damos opcion para crear cuenta  */}
        <Link to='/register'>Need an account?</Link>
        </>

    )
}