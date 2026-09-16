import DashboardLayout from "../layouts/DashboardLayout";
import { Typography } from "@mui/material";
import { useAuth } from "../context/AuthContext";

function Dashboard() {

    const { user } = useAuth();

    return (

        <DashboardLayout>

            <Typography variant="h4">

                Dashboard

            </Typography>

            <Typography mt={2}>

                Welcome {user?.username}

            </Typography>

        </DashboardLayout>

    );

}

export default Dashboard;