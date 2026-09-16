import {
    AppBar,
    Toolbar,
    Typography,
    Button
} from "@mui/material";

import { useNavigate } from "react-router-dom";
import { logout } from "../services/authService";
import { useAuth } from "../context/AuthContext";

function Navbar() {

    const navigate = useNavigate();

    const { setUser } = useAuth();

    async function handleLogout() {

        await logout();

        setUser(null);

        navigate("/");

    }

    return (

        <AppBar position="static">

            <Toolbar>

                <Typography
                    variant="h6"
                    sx={{ flexGrow: 1 }}
                >

                    Student Management System

                </Typography>

                <Button
                    color="inherit"
                    onClick={handleLogout}
                >

                    Logout

                </Button>

            </Toolbar>

        </AppBar>

    );

}

export default Navbar;