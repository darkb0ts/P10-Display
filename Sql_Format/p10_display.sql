-- phpMyAdmin SQL Dump
-- version 5.2.1deb1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Aug 07, 2024 at 12:22 PM
-- Server version: 10.11.6-MariaDB-0+deb12u1
-- PHP Version: 8.2.20

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `p10_display`
--

-- --------------------------------------------------------

--
-- Table structure for table `Display_Data`
--

CREATE TABLE `Display_Data` (
  `id` int(11) NOT NULL,
  `text` varchar(255) NOT NULL,
  `audio` varchar(255) NOT NULL,
  `scrolling` int(11) NOT NULL,
  `blink` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Display_Data`
--

INSERT INTO `Display_Data` (`id`, `text`, `audio`, `scrolling`, `blink`) VALUES
(1, 'Welcome to Magneto Dynamic ', 'luffy', 0, 1),
(2, 'CandyScooby', 'naruto', 0, 1),
(3, 'P10-Led Display Ip: 192.168.1.14', 'hello', 0, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Display_Data`
--
ALTER TABLE `Display_Data`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Display_Data`
--
ALTER TABLE `Display_Data`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
