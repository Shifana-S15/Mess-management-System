-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 18, 2024 at 06:31 PM
-- Server version: 11.6.1-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mess`
--

-- --------------------------------------------------------

--
-- Table structure for table `base_mess_menu_schedule`
--

CREATE TABLE `base_mess_menu_schedule` (
  `id` bigint(20) NOT NULL,
  `day` varchar(10) NOT NULL,
  `year` varchar(9) NOT NULL,
  `breakfast` longtext NOT NULL,
  `lunch` longtext NOT NULL,
  `snacks` longtext NOT NULL,
  `dinner` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `base_mess_menu_schedule`
--

INSERT INTO `base_mess_menu_schedule` (`id`, `day`, `year`, `breakfast`, `lunch`, `snacks`, `dinner`) VALUES
(1, 'Monday', '2024-2025', 'Idly, paasi parupu vegetable sambar,podi,coconut chutney,mint chutney/tomato chutney ,vada,coffee and milk', 'Tomato rice&sambar/lemon rice &sambar/tamarind rice& thuvvaiyal/coconut rice&thuvvaiyal, curd rice,pappad,pickle ', 'Roasted groundnut,ginger tea & milk', 'Chappathi,mushroom gravy/channa gravy,curd onion raita ,pickle ,boiled egg'),
(2, 'Tuesday', '2024-2025', 'Venn pongal,thuvaram paruppu vegetable sambar,coconut chutney,medhu vada ,coffee & milk', 'Rice,sambar,brinjal/beetroot/cabbage fry,rasam, butter milk,pappad,pickle', 'Valaikai bajji (2)/chilly bajji (2), coconut chutney,tea & milk', 'Special Dosa,mint chutney,coconut chutney,podi,banana,icecream '),
(3, 'Wednesday', '2024-2025', 'Plain bread,butter,pineapple jam,egg omlet,yeppi noodles/ kichadi,coffee & milk', 'Rice,paruppu+ghee,potato/pattani fry,rasam,butter milk,pappad&pickle', 'Paruppu vada,ginger tea&milk', 'Idly,kara chutney,sambar,podi,banana'),
(4, 'Thursday', '2024-2025', 'Dosa,brinjal vegetable sambar,podi,ghee sakkara pongal,kara chutney,coffee&milk', 'Vegetable bread briyani,meal maker gravy ,curd rice,onion raita&pickle', 'Boiled grams,tea&milk', 'Chappathi,panner butter masala,onion raita ,pickle,boiled egg&badam milk'),
(5, 'Friday', '2024-2025', 'Idly,vegetable sambar,podi,mint chutney,bonda,coffee&milk', 'Rice,vegetable sambar,carrot beans masala,rasam,butter milk,payasam,pappad&pickle', 'Medhu vada,ginger tea&milk', 'Curry leaves rice/mint rice,ellu thuvaiyal,omlet,curd rice,ice cream&banana'),
(6, 'Saturday', '2024-2025', 'Dosa,tomato chutney/mint chutney,rava kesari,coffee&milk', 'Rice,vatha kolambu,senai kizhangu fry,rasam,curd,pappad&pickle', 'Onion pakkoda,tea&milk', 'Plain bread,butter,pineapple jam,egg omlet,noodles,rosemilk'),
(7, 'Sunday', '2024-2025', 'Special ghee dosa,vegetable sambar,cocunut chutney,coffee&milk', 'Mushroom briyani,onion raita,gobi 65/bread halwa,rice,curd,pickle&lemon juice', 'Potato bajji,ginger tea&milk', 'Parotta,salna,rice,curd,pickle&banana');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `base_mess_menu_schedule`
--
ALTER TABLE `base_mess_menu_schedule`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `base_mess_menu_schedule`
--
ALTER TABLE `base_mess_menu_schedule`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
