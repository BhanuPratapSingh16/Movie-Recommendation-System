import { Link } from "react-router-dom";
import Navbar from "../components/Navbar";

export default function Home() {

    const user = JSON.parse(localStorage.getItem("user"));

    return (
        <>
            <Navbar />

            <div className="container mt-5">

                <div className="text-center mb-5">

                    <h1>
                        Welcome, {user?.name}! 👋
                    </h1>

                    <p className="text-muted fs-5">
                        Discover movies you'll love with personalized recommendations.
                    </p>

                </div>

                <div className="row g-4">

                    <div className="col-md-6">
                        <div className="card shadow h-100">

                            <div className="card-body text-center">

                                <h3>🔍 Search Movies</h3>

                                <p className="text-muted">
                                    Search movies and rate the ones you've watched.
                                </p>

                                <Link
                                    to="/search"
                                    className="btn btn-primary"
                                >
                                    Search
                                </Link>

                            </div>

                        </div>
                    </div>

                    <div className="col-md-6">
                        <div className="card shadow h-100">

                            <div className="card-body text-center">

                                <h3>⭐ Recommendations</h3>

                                <p className="text-muted">
                                    Get AI-powered personalized movie recommendations.
                                </p>

                                <Link
                                    to="/recommendations"
                                    className="btn btn-success"
                                >
                                    View Recommendations
                                </Link>

                            </div>

                        </div>
                    </div>

                </div>

            </div>
        </>
    );
}