import { useEffect } from "react"
import useGlobalReducer from "../hooks/useGlobalReducer"
import userServices from "../services/userServices"


export const Private = () => {

    const { store, dispatch } = useGlobalReducer()

    //traernos la info del usuario sin necesidad de hacer click en el boton de home
    // teniendo el token en el localStorage

    // useEffect(()=>{
    //    userServices.getUserInfo().then(data=> {
    //     localStorage.setItem('user', JSON.stringify(data))
    //     dispatch({type: 'get_user_info', payload: data})
    // })

    // },[])


    const handleLogout = () => {
        dispatch({ type: 'logout' })
    }

    return (
        <>
            <h2>this is private!!!!</h2>
            <h3>only for the eyes of: {store.user?.email}</h3>

            <button onClick={handleLogout}>logout</button>
        </>
    )
}