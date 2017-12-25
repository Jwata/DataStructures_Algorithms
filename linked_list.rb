class LinkedList
  attr_accessor :head

  def initialize
    self.head = nil
  end

  # add to head
  def add(value)
    current_head = head
    self.head = Node.new(value, current_head)
  end

  # delete from head
  def delete(value)
    current = head
    previous = nil

    while current != nil
      if current.value == value
        if previous
          previous.next = current.next
        else
          self.head = current.next
        end
      end
      previous = current
      current = current.next
    end
  end

  def size
    count = 0
    current = head

    while current != nil
      current = current.next
      count += 1
    end

    count
  end

  def to_array
    array = []
    current = head
    while current != nil
      array << current.value
      current = current.next
    end
    array
  end
end

class Node
  attr_accessor :value, :next

  def initialize(value, next_node)
    self.value = value
    self.next = next_node
  end
end
