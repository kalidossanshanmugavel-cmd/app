import { Drawer, List, ListItemButton, ListItemText } from "@mui/material";
import { Link } from "react-router-dom";

function Sidebar() {

    return (

        <Drawer
            variant="permanent"
            sx={{
                width: 220,
                "& .MuiDrawer-paper": {
                    width: 220,
                    boxSizing: "border-box",
                },
            }}
        >

            <List>

                <ListItemButton component={Link} to="/dashboard">

                    <ListItemText primary="Dashboard" />

                </ListItemButton>

                <ListItemButton component={Link} to="/students">

                    <ListItemText primary="Students" />

                </ListItemButton>

            </List>

        </Drawer>

    );

}

export default Sidebar;