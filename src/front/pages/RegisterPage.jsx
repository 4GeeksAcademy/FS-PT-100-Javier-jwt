import { Link } from "react-router-dom"
import { Register } from "../components/register"

export const RegisterPage = () => {


    return (
        <>
            <Register />
            {/* si estamos en vista de registro y ya tenemos una cuenta, lo podemos pasar a login */}
            <Link to='/login'>Already registered?</Link>

        </>
    )
} 