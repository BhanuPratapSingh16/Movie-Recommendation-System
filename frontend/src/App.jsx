import './App.css'
import Navbar from './components/Navbar'
import Register from './pages/Register'
import Login from './pages/Login'
import { Routes, Route } from 'react-router-dom'
import Home from './pages/Home'
import Search from './pages/Search'
import Recommendations from './pages/Recommendations'
import ProtectedRoute from './components/ProtectedRoute'

function App() {

  return (
    <>
      <Routes>
          <Route path="/" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/home" element={<ProtectedRoute> <Home /> </ProtectedRoute>}/>
          <Route path="/search" element={<ProtectedRoute> <Search/> </ProtectedRoute> }/>
          <Route path="/recommendations" element={<ProtectedRoute> <Recommendations/> </ProtectedRoute> }/>
      </Routes>
    </>
  )
}

export default App
