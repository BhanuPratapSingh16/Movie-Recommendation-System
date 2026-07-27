import { Link, useNavigate } from "react-router-dom";

export default function Navbar() {

    const navigate = useNavigate();

    const user = JSON.parse(localStorage.getItem("user"));

    const logout = () => {
        localStorage.clear();
        navigate("/");
    };

    return (
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark shadow">
            <div className="container">

                <Link className="navbar-brand fw-bold" to="/home">
                    🎬 MovieAI
                </Link>

                <button
                    className="navbar-toggler"
                    type="button"
                    data-bs-toggle="collapse"
                    data-bs-target="#navbarNav"
                >
                    <span className="navbar-toggler-icon"></span>
                </button>

                <div className="collapse navbar-collapse" id="navbarNav">

                    <ul className="navbar-nav me-auto">

                        <li className="nav-item">
                            <Link className="nav-link" to="/home">
                                Home
                            </Link>
                        </li>

                        <li className="nav-item">
                            <Link className="nav-link" to="/search">
                                Search Movies
                            </Link>
                        </li>

                        <li className="nav-item">
                            <Link className="nav-link" to="/recommendations">
                                Recommendations
                            </Link>
                        </li>

                    </ul>

                    <span className="navbar-text me-3">
                        👋 {user?.name}
                    </span>

                    <button
                        className="btn btn-outline-light"
                        onClick={logout}
                    >
                        Logout
                    </button>

                </div>

            </div>
        </nav>
    );
}