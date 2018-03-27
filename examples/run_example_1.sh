bash script_0.sh&
bash script_2.sh&
pipe-scripts --waited_scripts script_0.sh script_1.sh --future_scripts script_1.sh script_2.sh script_3.sh
