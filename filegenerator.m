trials = 100;
accuracy = [0, 1];
%Let 0 = miss, 1 = hit
voltRange = 500;
channel = 32;
time_intervals = 100;
time_start = 100;



% For each channel:
      %For a certain period of time
        % Generate Random Voltage with an upperbound of 500
               %associate with that a hit and miss for auditory and visual


fileID = fopen('pseudo_eeg_data.txt','w');
fprintf(fileID,'%6s %12s %18s %24s %30s \n','Trial', 'Hit/Miss', 'Channel','Time', 'Voltage');
for t = 1: trials
    acc = randi([0,1],1,1);
    for c = 1: channel
        for r = time_start: time_intervals:10000
            randVoltage = randi([0,voltRange],1,1);
            fprintf(fileID, '%6i %12i %18i %24i %30f \n', t, acc,  c, r, randVoltage); 
        end
    end
end
%fprintf(fileID,'%6.2f %12.8f\n',A);
fclose(fileID);