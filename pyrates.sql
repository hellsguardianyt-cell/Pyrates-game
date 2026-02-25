-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 12, 2025 at 07:33 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pyrates`
--

-- --------------------------------------------------------

--
-- Table structure for table `leaderboard`
--

CREATE TABLE `leaderboard` (
  `name` varchar(30) NOT NULL,
  `score` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `leaderboard`
--

INSERT INTO `leaderboard` (`name`, `score`) VALUES
('Aaryan', 76),
('Aaryan', 442),
('Sahil', 214),
('aaaa', 76),
('Aar', 446),
('Player', 167),
('asasas', 1),
('hoho', 0),
('aa', 0),
('haha', 76),
('Aaryan', 126);

-- --------------------------------------------------------

--
-- Table structure for table `level_leaderboard`
--

CREATE TABLE `level_leaderboard` (
  `id` int(11) NOT NULL,
  `level` int(11) NOT NULL,
  `user_name` varchar(255) NOT NULL,
  `score` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp() CHECK (`level` > 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `level_leaderboard`
--

INSERT INTO `level_leaderboard` (`id`, `level`, `user_name`, `score`, `created_at`) VALUES
(1, 5, 'aaaa', 76, '2025-03-10 12:09:14'),
(2, 5, 'Bihari Ji', 76, '2025-03-10 12:11:18'),
(3, 1, 'Aar', 60, '2025-03-10 12:16:29'),
(4, 2, 'Aar', 139, '2025-03-10 12:17:25'),
(5, 3, 'Aar', 76, '2025-03-10 12:17:38'),
(6, 4, 'Aar', 90, '2025-03-10 12:18:45'),
(7, 5, 'Aar', 76, '2025-03-10 12:18:57'),
(8, 1, 'Player', 31, '2025-03-10 12:27:18'),
(9, 2, 'Player', 122, '2025-03-10 12:27:38'),
(10, 3, 'Player', 1, '2025-03-10 12:27:45'),
(11, 4, 'Player', 8, '2025-03-10 12:28:00'),
(12, 5, 'Player', 0, '2025-03-10 12:28:07'),
(13, 5, 'asasas', 1, '2025-03-10 12:29:10'),
(14, 5, 'hoho', 0, '2025-03-10 12:34:57'),
(15, 5, 'aa', 0, '2025-03-10 12:36:05'),
(16, 5, 'haha', 76, '2025-03-10 12:39:41'),
(17, 1, 'Shalva', 220, '2025-03-11 08:21:20'),
(18, 2, 'Shalva', 153, '2025-03-11 08:22:05'),
(19, 3, 'Shalva', 54, '2025-03-11 08:22:23'),
(20, 1, 'Aary', 100, '2025-03-12 10:47:59'),
(21, 2, 'Aary', 127, '2025-03-12 10:48:50'),
(22, 5, 'Aaryan', 126, '2025-03-12 10:52:31'),
(23, 1, 'shush', 190, '2025-03-12 14:07:47');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `level_leaderboard`
--
ALTER TABLE `level_leaderboard`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `level_leaderboard`
--
ALTER TABLE `level_leaderboard`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
