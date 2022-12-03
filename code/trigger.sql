CREATE DEFINER=`root`@`%` TRIGGER `Forum_BEFORE_INSERT` BEFORE INSERT ON `Forum` FOR EACH ROW BEGIN
	SET @title = REPLACE(New.post_title, 'fuck', '****');
    SET @content = REPLACE(New.post_content, 'fuck', '****');
   
    SET New.post_title = @title;
    SET New.post_content = @content;
END