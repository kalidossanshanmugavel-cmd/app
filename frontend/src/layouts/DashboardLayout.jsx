import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";
import { Box } from "@mui/material";

function DashboardLayout({ children }) {

    return (

        <Box sx={{ display: "flex" }}>

            <Sidebar />

            <Box sx={{ flexGrow: 1 }}>

                <Navbar />

                <Box sx={{ p: 3 }}>

                    {children}

                </Box>

            </Box>

        </Box>

    );

}

export default DashboardLayout;